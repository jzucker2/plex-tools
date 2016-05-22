#!/usr/bin/env python

import os
import glob
import shutil
from guessit import guessit
from utilities.media_collector import MediaFileCollector

television_directory_to_sort = '/Volumes/Xanadu-Plex/Test'
television_directory_to_sort = '/Users/jzucker/Desktop/Test'

class TelevisionSorter(object):
	"""docstring for TelevisionSorter"""
	def __init__(self, unsorted_television_directory):
		super(TelevisionSorter, self).__init__()
		self.television_directory = unsorted_television_directory
		self.collector = MediaFileCollector(self.television_directory)
	def sort(self):
		print 'sort'
		all_files = self.collector.all_files()
		for video_file in all_files:
			print video_file
			video_guess = guessit(video_file)
			print 'video_guess'
			print video_guess

def main():
	print 'television_sorter'
	sorter = TelevisionSorter(television_directory_to_sort)
	sorter.sort()
		

if __name__ == '__main__':
	main()
