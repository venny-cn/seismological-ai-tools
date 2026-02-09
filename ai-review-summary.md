# AI 审查报告：项目概览与核心功能

生成时间：2026-02-04

## 项目作用

本仓库为地震学相关的开源工具集合，面向自动化地震相位拾取、去噪、相位关联为事件、极化/断层机制分析与表面波色散标注，并提供交互式波形标注应用以支持人工复核与数据标注工作流。

## 主要模块与职责

- `seismic-event-detection`：相位拾取模型（BRNN、PhaseNet、LPPN、UNet++ 等）、TorchScript/ONNX 导出、以及相位关联器（REAL、LPPN/fastlinker、GaMMA）。
- `data-filter`：波形去噪模型与训练脚本（包含联合训练以在去噪后保持相位可拾取性）。
- `hdf5-dataset-tools`：从 MSEED 构建索引并生成 HDF5 数据集的工具（`makeindex.py`、`makeh5.py`、`testh5.py`）。
- `waveform-annotation-app`：基于 Streamlit 的交互式标注工具，支持 DNN 预标注、多台站可视化、色散手工标注并导出 JSON。
- 其他目录：包含训练脚本、模型对比、极化/断层机制工具、表面波色散实验等辅助代码与示例。

## 关键依赖（摘录）

- Python 科学栈：`numpy`, `pandas`, `scipy`, `h5py`
- 波形处理：`obspy` (>=1.4)
- 深度学习：`torch`（README/子模块建议 >=2.1 用于 app）
- 可视化/前端：`streamlit`, `plotly`, `streamlit-plotly-events`
- 部署/推理：`onnxruntime`（用于 ONNX 模型运行）
- 其他：`opencv`（README 提及）、`tqdm`、`sqlite`（索引用）

（具体依赖请参见各子模块下的 `requirements.txt` 或 README）

## 核心功能点与亮点

- 多架构相位拾取：BRNN、RNN(PnSn)、PhaseNet/UNet/UNet++、LPPN 等，提供训练检查点、TorchScript 与 ONNX 导出。
- 相位关联：提供多种关联器用于把拾取的相位聚合成地震事件（`reallinker.py`、`fastlinker.py`、`gammalinker.py`）。
- 去噪与联合训练：`data-filter` 支持训练去噪网络，并验证去噪后仍可保持相位拾取性能。
- 高效数据流水线：`hdf5-dataset-tools` 支持大规模 MSEED 索引与 HDF5 数据集构建，便于批量训练与评估。
- 交互式标注：Streamlit 应用可进行快速人工复核、DNN 预标注、色散分支交互标注并导出标准化 JSON。

## 快速运行示例

运行相位拾取（示例，需在 `seismic-event-detection` 下运行或调整路径）：

```bash
python picker.py -i path/to/data -o output_name -m pickers/rnn.jit -d cpu
```

启动标注应用（在 `waveform-annotation-app` 目录）：

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 建议的后续动作

- 如需在本地快速部署标注应用，请生成并安装合并依赖（可由维护者确认版本），或我可以为你生成 `requirements-merged.txt`。
- 若需把特定子模块单独打包或导出 ONNX 模型，我可以进一步列出每个模型的文件位置与使用说明。

---

文件已生成：docs/logs/ai-review-reports/ai-review-summary.md
