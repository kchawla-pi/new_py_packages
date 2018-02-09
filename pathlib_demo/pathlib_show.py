from pathlib import Path
from pprint import pprint


rootpath_str = '~\\OneDrive\\workspace\\new_py_packages\\demo_tree'
rootpath = Path(rootpath_str).expanduser()


def show_path():
	print('\n', rootpath_str)
	
	print(Path(rootpath_str))
	
	print('\n', rootpath)
# show_path()


def show_parent():
	print('\n', rootpath.parent)
	
	print('\n',
	      rootpath.parents[0],
	      rootpath.parents[1],
	      rootpath.parents[2],
	      rootpath.parents[3],
	      rootpath.parents[4],
	      sep='\n')
# show_parent()


def show_iter():
	print()
	pprint(list(rootpath.iterdir()))
show_iter()


def show_filter():
	files = [entry for entry in rootpath.parent.iterdir() if entry.is_file() and 'workspace' in rootpath.parents]
	print()
	pprint(files)
# show_filter()


def show_join():
	print(rootpath.joinpath('demo_dir1', 'demo2.txt'))
# show_join()


filepath = rootpath.joinpath('demo_dir1', 'demo2.txt')


def show_file():
	print('\n',
	      filepath,
	      filepath.parent,
	      filepath.name,
	      filepath.stem,
	      filepath.suffix,
	      filepath.exists(),
	      filepath.is_file(),
	      filepath.is_dir(),
	      sep='\n')
# show_file()


def show_name_change():
	print('\n',
	      filepath.with_suffix('.tzr.gz'),
	      filepath.with_suffix('.tzr.gz').suffixes,
	      filepath.with_name('new_name.txt'),
	      sep='\n')
# show_name_change()


def show_samefile():
	print('\n',
	      filepath,
	      filepath.samefile(filepath.with_name('demo2.txt')),
	      sep='\n')
# show_samefile()


def show_glob():
	print('\n',
	      *filepath.parent.glob('*.*.*'),
	      sep='\n')

	print('\n',
	      *filepath.parent.glob('**/*.txt'),
	      sep='\n')
# show_glob()


def show_read():
	print()
	print(filepath.read_text())
# show_read()


def show_write():
	filepath.with_name('demo3.txt').write_text('woot woot')
	print(filepath.with_name('demo3.txt').read_text(errors='ignore'))
# show_write()


def show_rename():
	filepath.with_name('demo2_copy.txt').rename('demo2_copy_renamed.txt')
	print()
	pprint(list(filepath.iterdir()))
# show_rename()
