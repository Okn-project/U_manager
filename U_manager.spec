a = Analysis(
    ['src\\app\\application.py'],
    pathex=['C:\\Users\\Mission\\Desktop\\main\\proj\\U_manager'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PyQt5.sip',
        'PyQt5.QtCore',
        'PyQt5.QtGui',
        'PyQt5.QtWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt6',
        'PySide6',
        'qt6',
        'Qt6'],
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
    name='U_Manager',
    onefile=False,
    console=False,
)