#!/usr/bin/env python

import os
from guessit import guessit

directory_to_sort = '/Volumes/Xanadu-Plex/Old'
destination_directory = '/Volumes/Xanadu-Plex'

class MediaFileCollector(object):
	"""docstring for MediaFileCollector"""
	def __init__(self, sorting_directory):
		super(MediaFileCollector, self).__init__()
		self.sorting_directory = sorting_directory
	def all_files(self):
		return []

# automatically sorts movies into self.destination/Movies
# and tv shows into self.destination/Television
class Sorter(object):
	"""docstring for Sorter"""
	def __init__(self, destination):
		super(Sorter, self).__init__()
		self.destination = destination
	def get_television_subdirectory(self):
		return "blah"
	def get_movies_subdirectory(self):
		return "blah"
	def sort(self, unsorted_files):
		pass

		
		

def main():
	print "main"
	collector = MediaFileCollector(directory_to_sort)


if __name__ == "__main__":
	main()
