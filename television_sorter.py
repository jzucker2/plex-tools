#!/usr/bin/env python

import os
import glob
import shutil
from guessit import guessit
from utilities.media_collector import MediaFileCollector

television_directory_to_sort = '/Volumes/Xanadu-Plex/Television'
# television_directory_to_sort = '/Users/jzucker/Desktop/Test'

class TelevisionSorter(object):
	"""docstring for TelevisionSorter"""
	def __init__(self, unsorted_television_directory):
		super(TelevisionSorter, self).__init__()
		self.television_directory = unsorted_television_directory
		self.collector = MediaFileCollector(self.television_directory)
	def move_file(self, unsorted_file, destination_subdirectory):
		file_name = os.path.basename(unsorted_file)
		final_destination = os.path.join(destination_subdirectory, file_name)
		shutil.move(unsorted_file, final_destination)
	def sort(self):
		print 'sort'
		all_files = self.collector.all_files()
		print all_files
		for video_file in all_files:
			print 'this'
			print video_file
			try:
				video_guess = guessit(video_file)
				print 'video_guess'
				print video_guess
				show_name = video_guess['title']
				print show_name
				final_destination = os.path.join(self.television_directory, show_name)
				if not os.path.exists(final_destination):
					os.makedirs(final_destination)
				self.move_file(video_file, final_destination)
			except Exception, e:
				print 'exception'
				print e
				raise

def main():
	print 'television_sorter'
	sorter = TelevisionSorter(television_directory_to_sort)
	sorter.sort()
		

if __name__ == '__main__':
	main()
