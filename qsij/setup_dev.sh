#!/bin/bash
# qsij Development Setup Script

echo "CONFIG: Setting up qsij development environment..."

# Check if conda is available
if command -v conda &> /dev/null; then
    echo "PACKAGE: Creating conda environment..."
    conda env create -f environment.yml
    
    echo "SUCCESS: Conda environment created! Activate with:"
    echo "  conda activate qsij-quantum-env"
else
    echo "PACKAGE: Creating Python virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    
    # Install local quantumsim if available
    if [[ -d "../quantumsim" ]]; then
        echo "PACKAGE: Installing local quantumsim..."
        pip install -e ../quantumsim
    fi
    
    echo "SUCCESS: Virtual environment created! Activate with:"
    echo "  source .venv/bin/activate"
fi

echo ""
echo "SUCCESS: Development environment ready!"
echo "  Start the server with: ./start_quantum_server.sh"