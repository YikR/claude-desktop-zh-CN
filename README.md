# Claude Desktop 中文语言包 🇨🇳

为 Claude Desktop 添加简体中文界面支持。

## 效果

安装后在 Claude Desktop 的 Settings → Language 中选择 **中文（中国大陆）**，界面即切换为中文。

## 安装方法

### 自动安装

```bash
git clone https://github.com/YikR/claude-desktop-zh-CN.git
cd claude-desktop-zh-CN
python3 install.py
```

然后完全退出并重启 Claude Desktop。

### 手动安装

将以下文件复制到对应位置：

| 源文件 | 目标位置 |
|--------|----------|
| `i18n/zh-CN.json` | `/Applications/Claude.app/Contents/Resources/ion-dist/i18n/zh-CN.json` |
| `i18n/zh-CN.overrides.json` | `/Applications/Claude.app/Contents/Resources/ion-dist/i18n/zh-CN.overrides.json` |
| `i18n/statsig/zh-CN.json` | `/Applications/Claude.app/Contents/Resources/ion-dist/i18n/statsig/zh-CN.json` |
| `zh-CN.json` | `/Applications/Claude.app/Contents/Resources/zh-CN.json` |
| `Localizable.strings` | `/Applications/Claude.app/Contents/Resources/zh-CN.lproj/Localizable.strings` |

## 翻译说明

- 基于日语语言包（ja-JP）翻译而来
- 总计 **14,091 条** UI 文本已翻译
- 完成了桌面端主界面、设置、扩展、通知等所有模块
- 翻译完成度 **99.5%**

## 版本兼容

- Claude Desktop for macOS
- 基于版本 1.8089.1 开发
- 可能需要随 Claude Desktop 更新而更新翻译文件

## 致谢

翻译工作由 Claude (Anthropic) 协助完成。
