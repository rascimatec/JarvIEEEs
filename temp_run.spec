# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['temp_run.py'],
             pathex=['C:\\Users\\J. Gabriel\\Documents\\GitHub\\JarvIEEEs\\Geral', 'C:\\Users\\J. Gabriel\\Documents\\GitHub\\JarvIEEEs\\lib\\chatterbot_corpus\\data\\portuguese', 'C:\\Users\\J. Gabriel\\Documents\\GitHub\\JarvIEEEs'],
             binaries=[],
             datas=[],
             hiddenimports=['chatterbot_corpus'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='temp_run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
