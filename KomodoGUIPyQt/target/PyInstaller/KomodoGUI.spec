# -*- mode: python -*-

block_cipher = None


a = Analysis(['/home/rohit/PycharmProjects/KomodoGUIPyQt/src/main/python/main.py'],
             pathex=['/home/rohit/PycharmProjects/KomodoGUIPyQt/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/home/rohit/PycharmProjects/KomodoGUIPyQt/venv/lib/python3.5/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/tmp/tmp9r2t2zs9/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='KomodoGUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='KomodoGUI')
