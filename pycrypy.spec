# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/cli/main.py'],
    pathex=[],
    binaries=[],
    datas=[('./src/light_themes', 'light_themes'), ('./src/dark_themes', 'dark_themes'), ('./src/recommended_themes', 'recommended_themes'), ('./src/cli', 'cli'), ('./src/config', 'config'), ('./src/lib', 'lib')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pycrypy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
