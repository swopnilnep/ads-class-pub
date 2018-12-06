'''
Swopnil N. Shrestha
CS-160
05/12/2018
'''

"""Using Breadth first search to find Kevin Bacon's number of actors"""
#!/usr/bin/env python3
# encoding: UTF-8

import sys
import time
from pythonds3 import Graph, Vertex, Queue

def read_file(filename):
    movie_dict = {}
    bg = Graph()
    for item in open(filename, 'r'):
        # Clean the data
        temp = item.split('|')
        temp[1] = temp[1].strip('\n')
        movie = temp[0]
        
        # Build movie dictionary
        if movie in movie_dict: movie_dict[movie].append(temp[1])
        else: movie_dict[movie] = [temp[1]]
                          
    for item in movie_dict.keys():
        for actor1 in movie_dict[item]:
            for actor2 in movie_dict[item]:
                if actor1 != actor2:
                    bg.add_edge(actor1, actor2, item)
    return bg
    
def traverse(x, goal):
    bacon_list = []
    stop = False
    while (x.get_previous()) and stop == False:
        bacon_list.append(x)
        x = x.get_previous()
        if x == goal:
            stop = True
    bacon_list.append(x)
    return bacon_list
    
def main():
    print("\n---Kevin Bacon Number Calculator---")
    print("\nReading the file..", end="")
    
    '''Setup the Graph'''
    bacon = read_file('data/projects/kevinbacon/movie_actors_test.txt')
    # bacon = read_file('data/projects/kevinbacon/movie_actors_full.txt')

    # Run the breadth first search
    bacon.bfs(bacon.get_vertex('Kevin Bacon'))
    
    print("\nReading Complete")
    print("="*40)

    '''Run the program'''
    run = True
    while run:
        search_field = input("\nWhat actor would you like to trace? ('exit' to quit): ")
        search_field = search_field.title()
        
        try:
            if str.lower(search_field) in ('exit','quit','stop','end'):
                run = False
            elif search_field == 'Kevin Bacon':
                print("Kevin Bacon's Bacon number is 0.")
            else:
                bacon_list = traverse(bacon.get_vertex(search_field), bacon.get_vertex('Kevin Bacon'))
                print("The Kevin Bacon Number for {} is {}".format(search_field, len(bacon_list) - 1))
                for i in range(len(bacon_list) - 1):
                    neighbor = bacon_list[i].get_neighbor(bacon_list[i + 1])
                    print(bacon_list[i].get_key(), 'worked with', bacon_list[i + 1].get_key(), 'in', neighbor)
        except:
            print(search_field, "does not have a Bacon number.")

if __name__=="__main__":
    main()