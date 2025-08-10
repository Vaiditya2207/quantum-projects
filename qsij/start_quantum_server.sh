#!/bin/bash
# qsij - Quantum Simulator Interactive Jupyter Server
# One-click startup script for quantum computing education

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Default configuration
DEFAULT_PORT=3032
JUPYTER_PORT=${JUPYTER_PORT:-$DEFAULT_PORT}
DEV_MODE=false
SHARE_MODE=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dev)
            DEV_MODE=true
            shift
            ;;
        --share)
            SHARE_MODE=true
            shift
            ;;
        --port)
            JUPYTER_PORT="$2"
            shift 2
            ;;
        -h|--help)
            echo "qsij - Quantum Simulator Interactive Jupyter"
            echo ""
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --port PORT    Set custom port (default: 3032)"
            echo "  --dev          Development mode with auto-reload"
            echo "  --share        Allow external connections (use with caution)"
            echo "  -h, --help     Show this help message"
            echo ""
            echo "Examples:"
            echo "  $0             # Start on default port 3032"
            echo "  $0 --port 8888    # Start on port 8888"
            echo "  $0 --dev          # Development mode"
            echo "  JUPYTER_PORT=9999 $0    # Set port via environment"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use $0 --help for usage information"
            exit 1
            ;;
    esac
done

echo -e "${PURPLE}Starting qsij - Quantum Simulator Interactive Jupyter${NC}"
echo -e "${CYAN}======================================================${NC}"

# Check if we're in the right directory
if [[ ! -f "start_quantum_server.sh" ]]; then
    echo -e "${RED}ERROR: Please run this script from the qsij directory${NC}"
    echo -e "${YELLOW}  cd /path/to/qsij && ./start_quantum_server.sh${NC}"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check if port is available
port_available() {
    ! nc -z localhost $1 2>/dev/null
}

# Check Python installation
echo -e "${BLUE}SEARCH: Checking Python installation...${NC}"
if command_exists python3; then
    PYTHON_CMD=python3
elif command_exists python; then
    PYTHON_CMD=python
else
    echo -e "${RED}ERROR: Python not found. Please install Python 3.8+${NC}"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
echo -e "${GREEN}SUCCESS: Found Python $PYTHON_VERSION${NC}"

# Check if port is available  
echo -e "${BLUE}SEARCH: Checking port $JUPYTER_PORT...${NC}"
if ! port_available $JUPYTER_PORT; then
    echo -e "${YELLOW}WARNING: Port $JUPYTER_PORT is already in use${NC}"
    echo -e "${YELLOW}  Try a different port: ./start_quantum_server.sh --port 8888${NC}"
    exit 1
fi
echo -e "${GREEN}SUCCESS: Port $JUPYTER_PORT is available${NC}"

# Create virtual environment if it doesn't exist
if [[ ! -d ".venv" ]]; then
    echo -e "${BLUE}CONFIG: Creating Python virtual environment...${NC}"
    $PYTHON_CMD -m venv .venv
    echo -e "${GREEN}SUCCESS: Virtual environment created${NC}"
fi

# Activate virtual environment
echo -e "${BLUE}CONFIG: Activating virtual environment...${NC}"
source .venv/bin/activate

# Install dependencies
echo -e "${BLUE}PACKAGE: Installing dependencies...${NC}"
if [[ ! -f ".deps_installed" ]] || [[ "$DEV_MODE" == true ]]; then
    echo -e "${CYAN}  Installing quantumsim and Jupyter...${NC}"
    
    # Install local quantumsim first
    if [[ -d "../quantumsim" ]]; then
        echo -e "${CYAN}  Installing local quantumsim from ../quantumsim${NC}"
        pip install -e ../quantumsim
    else
        echo -e "${CYAN}  Installing quantumsim from requirements${NC}"
        pip install quantumsim-edu
    fi
    
    # Install Jupyter and other dependencies
    pip install -r requirements.txt
    
    # Install Jupyter extensions for better experience
    jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build 2>/dev/null || true
    jupyter lab build 2>/dev/null || echo "Lab build skipped"
    
    touch .deps_installed
    echo -e "${GREEN}SUCCESS: Dependencies installed${NC}"
else
    echo -e "${GREEN}SUCCESS: Dependencies already installed${NC}"
fi

# Create notebooks directory if it doesn't exist
if [[ ! -d "notebooks" ]]; then
    echo -e "${BLUE}DOCS: Creating notebooks directory...${NC}"
    mkdir -p notebooks
    echo -e "${GREEN}SUCCESS: Notebooks directory created${NC}"
fi

# Set up Jupyter configuration
echo -e "${BLUE}CONFIG: Configuring Jupyter server...${NC}"
mkdir -p server
export JUPYTER_CONFIG_DIR="$(pwd)/server"

# Create Jupyter config
cat > server/jupyter_lab_config.py << EOF
# qsij Jupyter Lab Configuration
c = get_config()

# Server settings
c.ServerApp.port = $JUPYTER_PORT
c.ServerApp.open_browser = True
c.ServerApp.root_dir = '$(pwd)/notebooks'
c.ServerApp.notebook_dir = '$(pwd)/notebooks'

# Security settings
c.ServerApp.token = ''
c.ServerApp.password = ''

if not $SHARE_MODE:
    c.ServerApp.ip = 'localhost'
else:
    c.ServerApp.ip = '0.0.0.0'

# Performance settings
c.ServerApp.max_buffer_size = 268435456  # 256MB

# UI settings
c.LabApp.default_url = '/lab'
EOF

# Display startup information
echo -e "${CYAN}======================================================${NC}"
echo -e "${GREEN}SUCCESS: qsij Quantum Learning Environment Ready!${NC}"
echo -e "${CYAN}======================================================${NC}"
echo -e "${YELLOW}  Server URL: ${BLUE}http://localhost:$JUPYTER_PORT${NC}"
echo -e "${YELLOW}  Notebooks: ${BLUE}$(pwd)/notebooks${NC}"
echo -e "${YELLOW}  Config: ${BLUE}$(pwd)/server${NC}"

if [[ "$SHARE_MODE" == true ]]; then
    echo -e "${YELLOW}  External Access: ${RED}ENABLED (use with caution)${NC}"
fi

if [[ "$DEV_MODE" == true ]]; then
    echo -e "${YELLOW}  Development Mode: ${GREEN}ENABLED${NC}"
fi

echo -e "${CYAN}======================================================${NC}"
echo -e "${PURPLE}  Starting Jupyter Lab...${NC}"
echo -e "${CYAN}  Press Ctrl+C to stop the server${NC}"
echo -e "${CYAN}======================================================${NC}"

# Start Jupyter Lab
jupyter lab \
    --config=server/jupyter_lab_config.py \
    --no-browser \
    --allow-root \
    2>/dev/null || {
    echo -e "${RED}ERROR: Failed to start Jupyter Lab${NC}"
    echo -e "${YELLOW}  Try running: pip install --upgrade jupyterlab${NC}"
    exit 1
}