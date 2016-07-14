#!/usr/bin/env python

from utilities.media_collector import MediaFileCollector

# directory_to_sort = '/Volumes/Xanadu-Plex/Old'
# destination_directory = '/Volumes/Xanadu-Plex'
directory_to_sort = '/Volumes/Xanadu-Plex/Old'
destination_directory = '/Volumes/Xanadu-Plex'

class LooneyTunesSorter(object):
	"""docstring for LooneyTunesSorter"""
	def __init__(self, arg):
		super(LooneyTunesSorter, self).__init__()
		self.arg = arg
		
