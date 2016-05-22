#!/usr/bin/env python

import os
import shutil
from guessit import guessit
from utilities.media_collector import MediaFileCollector

# directory_to_sort = '/Volumes/Xanadu-Plex/Old'
# destination_directory = '/Volumes/Xanadu-Plex'
directory_to_sort = '/Volumes/Xanadu-Plex/Old'
destination_directory = '/Volumes/Xanadu-Plex'

# automatically sorts movies into self.destination/Movies
# and tv shows into self.destination/Television
class Sorter(object):
	"""docstring for Sorter"""
	def __init__(self, destination):
		super(Sorter, self).__init__()
		self.destination = destination
	def get_television_directory(self):
		return os.path.join(self.destination, "Television")
	def get_movies_directory(self):
		return os.path.join(self.destination, "Movies")
	def create_subdirectories_if_necessary(self, subdirectory):
		if not os.path.exists(subdirectory):
			os.makedirs(subdirectory)
	def move_file(self, unsorted_file, destination_subdirectory):
		file_name = os.path.basename(unsorted_file)
		final_destination = os.path.join(destination_subdirectory, file_name)
		shutil.move(unsorted_file, final_destination)
	def sort(self, unsorted_files):
		# first create Movies and Television subdirectories if they don't exist
		movies_destination = self.get_movies_directory()
		tv_destination = self.get_television_directory()
		self.create_subdirectories_if_necessary(movies_destination)
		self.create_subdirectories_if_necessary(tv_destination)
		for video_file in unsorted_files:
			video_guess = guessit(video_file)
			if video_guess['type'] == 'movie':
				# move to movies
				self.move_file(video_file, movies_destination)
			elif video_guess['type'] == 'episode':
				# move to tv
				self.move_file(video_file, tv_destination)
			else:
				print '--------------------------'
				print 'Unknown type encountered'
				print video_guess
				print '--------------------------'

		
		

def main():
	print "Sorting media ..."
	collector = MediaFileCollector(directory_to_sort)
	sorter = Sorter(destination_directory)
	sorter.sort(collector.all_files())
	


if __name__ == "__main__":
	main()
