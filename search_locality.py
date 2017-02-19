from __future__ import print_function  # Python 2/3 compatibility
import argparse
import string
import os
import sys

__author__ = "Stephen Goncher"
__copyright__ = "Copyright 2017, Stelligent Systems, LLC"


def get_args():
    parser = argparse.ArgumentParser(description='Searches for terms within N \
        context amount for text files in a directory, returning a list of \
        matching text files')
    parser.add_argument('term_1', help='first term to search for (phrases must \
        be double quoted)')
    parser.add_argument('term_2', help='second term to search for (phrases must \
        be double quoted)')
    parser.add_argument('context', type=int, nargs='?', default=1, help='size of context \
        N, where N is the number of words or less between the terms, \
        defaults to 1')
    parser.add_argument('dir_name', nargs='?', default='.', help='directory to \
        read plain text files from, defaults to current directory')
    return parser


def check_phrases(term, term_item, index, term_list, word_count):
    term_new = ''
    for i in range(word_count):
        # Modulus % prevents us from going out of range
        term_new += term_list[(index + i) % len(term_list)] + ' '
    return term_new.rstrip()


def parse_files(term_1, term_2, context, dir_name):
    file_list = []
    for file in os.listdir(dir_name):
        if file.endswith(".txt"):
            text = open(dir_name+"/"+file, "r").read()
            term_list = [word.strip(string.punctuation).lower() for
                         word in text.split()]
            result = find_terms(term_1, term_2, context, term_list, file)
            if result:
                file_list.append(file)
    return file_list


def find_terms(term_1, term_2, context, term_list, file):
    for index, item in enumerate(term_list):
        if ' ' in term_1:
            count_1 = len(term_1.split())
            check_1 = check_phrases(term_1, item, index, term_list, count_1)
        else:
            count_1 = 1
            check_1 = item
        if check_1 == term_1:
            for i in range(context+1):
                next_term = index + i + count_1
                # Modulus % prevents us from going out of range
                check_next = term_list[next_term % len(term_list)]
                if ' ' in term_2:
                    count_2 = len(term_2.split())
                    check_2 = check_phrases(term_2, check_next, next_term,
                                            term_list, count_2)
                else:
                    check_2 = check_next
                if check_2 == term_2:
                    return True
                    break


def main():
    file_list = []
    parser = get_args()
    args = parser.parse_args()
    file_list = parse_files(args.term_1.lower(), args.term_2.lower(),
                            args.context, args.dir_name)
    if not file_list:
        print("\nNo files found with matching search terms \
            in context given.\n")
    else:
        print()
        print(file_list)
        print()


if __name__ == '__main__':
    main()
