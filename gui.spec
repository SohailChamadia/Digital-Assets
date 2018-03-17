# -*- mode: python -*-

block_cipher = None


a = Analysis(['gui.py'],
             pathex=['C:\\Users\\sohai\\Documents\\GitHub\\digital-assets'],
             binaries=[],
             datas=[],
             hiddenimports=['peewee','ttk'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas+= Tree('C:\\Users\\sohai\\Documents\\GitHub\\digital-assets\\src', prefix='src\\')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gui',
          debug=False,
          strip=False,
          upx=True,
          console=False )
