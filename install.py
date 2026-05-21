#!/usr/bin/env python3
"""Claude Desktop 中文语言包安装脚本"""
import json, re, sys, os, shutil

CLAUDE_APP = '/Applications/Claude.app'
RESOURCES = f'{CLAUDE_APP}/Contents/Resources'
I18N_DIR = f'{RESOURCES}/ion-dist/i18n'
STATSIG_DIR = f'{I18N_DIR}/statsig'
ASSETS_DIR = f'{RESOURCES}/ion-dist/assets/v1'
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def check_app():
    if not os.path.exists(CLAUDE_APP):
        print(f'错误：未找到 Claude Desktop，请确认已安装到 {CLAUDE_APP}')
        sys.exit(1)
    print('✓ 已检测到 Claude Desktop')

def copy_i18n_files():
    print('\n安装翻译文件...')
    files = {
        f'{SCRIPT_DIR}/i18n/zh-CN.json': f'{I18N_DIR}/zh-CN.json',
        f'{SCRIPT_DIR}/i18n/zh-CN.overrides.json': f'{I18N_DIR}/zh-CN.overrides.json',
        f'{SCRIPT_DIR}/i18n/statsig/zh-CN.json': f'{STATSIG_DIR}/zh-CN.json',
        f'{SCRIPT_DIR}/zh-CN.json': f'{RESOURCES}/zh-CN.json',
        f'{SCRIPT_DIR}/Localizable.strings': f'{RESOURCES}/zh-CN.lproj/Localizable.strings',
    }
    for src, dst in files.items():
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            print(f'  ✓ {os.path.basename(dst)}')
        else:
            print(f'  ✗ 缺少文件: {src}')

def patch_js():
    print('\n注册中文语言...')
    # 在 index-DZuQva-j.js 中添加 zh-CN
    index_js = None
    for f in os.listdir(ASSETS_DIR):
        if f.startswith('index-') and f.endswith('.js'):
            index_js = f'{ASSETS_DIR}/{f}'
            break

    if index_js:
        with open(index_js, 'r') as f:
            content = f.read()

        # 添加 zh-CN 到语言列表
        old_list = '["en-US","de-DE","fr-FR","ko-KR","ja-JP","es-419","es-ES","it-IT","hi-IN","pt-BR","id-ID"]'
        new_list = '["en-US","de-DE","fr-FR","ko-KR","ja-JP","es-419","es-ES","it-IT","hi-IN","pt-BR","id-ID","zh-CN"]'

        if 'zh-CN' not in content:
            if old_list in content:
                content = content.replace(old_list, new_list)
                print('  ✓ 已添加 zh-CN 到语言列表')
            else:
                print('  ⚠ 语言列表格式已变化，可能需要手动更新')

        # 添加 zh-CN 到语言映射
        old_map = '"id-ID":"id"}'
        new_map = '"id-ID":"id","zh-CN":"zh-CN"}'
        if 'zh-CN":"zh-CN"' not in content:
            if old_map in content:
                content = content.replace(old_map, new_map)
                print('  ✓ 已添加 zh-CN 到语言映射')

        with open(index_js, 'w') as f:
            f.write(content)

    # 在 c284c2e59-DAjCHtgb.js 中注册 zh-CN
    for f in os.listdir(ASSETS_DIR):
        if 'c284c2e59' in f:
            js_path = f'{ASSETS_DIR}/{f}'
            with open(js_path, 'r') as fh:
                content = fh.read()
            old = 'case"id-ID":return["language","id"];default:return a'
            new = 'case"id-ID":return["language","id"];case"zh-CN":return["language","zh-CN"];default:return a'
            if 'zh-CN' not in content and old in content:
                content = content.replace(old, new)
                with open(js_path, 'w') as fh:
                    fh.write(content)
                print('  ✓ 已注册 zh-CN 语言代码')
            break

def verify():
    print('\n验证安装...')
    errors = []
    checks = [
        f'{I18N_DIR}/zh-CN.json',
        f'{I18N_DIR}/zh-CN.overrides.json',
        f'{STATSIG_DIR}/zh-CN.json',
        f'{RESOURCES}/zh-CN.json',
    ]
    for path in checks:
        if os.path.exists(path):
            print(f'  ✓ {os.path.basename(os.path.dirname(path))}/{os.path.basename(path)}')
        else:
            print(f'  ✗ 缺失: {path}')
            errors.append(path)

    if not errors:
        print(f'\n安装成功！请重启 Claude Desktop，然后在 Settings → Language 中选择"中文（中国大陆）"。')
    else:
        print(f'\n有 {len(errors)} 个文件缺失，请检查。')

def main():
    print('Claude Desktop 中文语言包安装器\n')
    if '--uninstall' in sys.argv:
        print('卸载功能暂未实现，请手动删除 zh-CN 相关文件。')
        return
    check_app()
    copy_i18n_files()
    patch_js()
    verify()

if __name__ == '__main__':
    main()
