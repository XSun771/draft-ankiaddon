# 安装说明

## 系统要求

- Anki 2.5.0 或更高版本
- Python 3.7+
- PyQt6

## 安装步骤

### 方法一：手动安装

1. **下载插件**
   - 下载整个插件文件夹
   - 确保包含以下文件：
     - `__init__.py`
     - `DraftWindow.py`
     - `meta.json`
     - `ui/` 目录及其内容

2. **找到 Anki 插件目录**
   - **Windows**: `%APPDATA%\Anki2\addons21\`
   - **macOS**: `~/Library/Application Support/Anki2/addons21/`
   - **Linux**: `~/.local/share/Anki2/addons21/`

3. **安装插件**
   - 将插件文件夹复制到 Anki 插件目录
   - 文件夹名称应该是 `draft-ankiaddon` 或类似名称

4. **重启 Anki**
   - 完全关闭 Anki
   - 重新启动 Anki

5. **启用插件**
   - 在 Anki 中，转到 工具 → 插件
   - 找到 "Draft Window" 插件
   - 确保插件已启用

### 方法二：使用 AnkiWeb（如果可用）

1. 访问 AnkiWeb 插件页面
2. 搜索 "Draft Window"
3. 点击安装
4. 重启 Anki

## 验证安装

1. 启动 Anki
2. 开始复习任何牌组
3. 应该会看到一个名为 "Draft Window" 的独立窗口弹出
4. 在文本框中输入内容
5. 切换到下一张卡片时，内容应该被重置

## 故障排除

### 插件不工作
- 检查 Anki 版本是否支持（需要 2.5.0+）
- 确认插件已启用
- 查看 Anki 的错误日志

### 窗口不显示
- 检查 PyQt6 是否正确安装
- 确认 UI 文件完整
- 重启 Anki

### 内容不重置
- 确认使用的是 `reviewer_did_show_question` 钩子
- 检查卡片切换逻辑

## 卸载

1. 在 Anki 中禁用插件：工具 → 插件 → 禁用 Draft Window
2. 删除插件文件夹
3. 重启 Anki

## 开发环境设置

如果你想修改插件：

1. 安装 Python 3.7+
2. 安装 PyQt6: `pip install PyQt6`
3. 安装 PyQt6-tools: `pip install PyQt6-tools`
4. 运行测试脚本: `python test_plugin.py`

## 支持

如果遇到问题，请：
1. 检查 Anki 版本
2. 查看错误日志
3. 在 GitHub 上提交 issue 