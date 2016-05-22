import os
import glob
import shutil
from guessit import guessit

# directory_to_sort = '/Volumes/Xanadu-Plex/Old'
# destination_directory = '/Volumes/Xanadu-Plex'
directory_to_sort = '/Volumes/Xanadu-Plex/Old'
destination_directory = '/Volumes/Xanadu-Plex'

class MediaFileCollector(object):
	"""docstring for MediaFileCollector"""
	def __init__(self, sorting_directory):
		super(MediaFileCollector, self).__init__()
		self.sorting_directory = sorting_directory
	def glob_file_pathname(self):
		return os.path.join(self.sorting_directory, "*.mp4")
	def all_files(self):
		return glob.glob(self.glob_file_pathname())
