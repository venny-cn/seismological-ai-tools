# 脚本执行脚本
# 创建推荐的Python 3.11环境
conda create -n seismic-env python=3.11
conda activate seismic-env

# 2. 使用 conda-forge 通道安装科学计算包
conda install -c conda-forge numpy scipy pandas matplotlib h5py obspy scikit-learn

# 3. 安装 numba
conda install numba

# 4. 使用 pip 安装 PyTorch 生态系统
pip install torch torchvision torchaudio

# 5. 安装其他必要的包
pip install streamlit plotly streamlit-plotly-events onnxruntime opencv-python tqdm
