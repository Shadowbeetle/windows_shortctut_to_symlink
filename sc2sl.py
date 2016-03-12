import codecs
import argparse
import os

import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", help="absolute path to the directory you wish to iterate",
                        type=str)
    parser.add_argument("old", help="part of path to be replaced, drive letter is necessary to be specified",
                        type=str)
    parser.add_argument("new", help="new path that replaces the old one",
                        type=str)
    parser.add_argument("-c", "--encoding", help="encoding of strings eg. in Eastern Europe it is usually "
                                                 "ISO-8859-2; defaults to ISO-8859-1")
    return parser.parse_args()


def main(root, old, new, encoding):
    for current_root, dirs, files in os.walk(root):
        links = filter(lambda s: s.endswith('.lnk'), files)
        for filename in links:
            path = os.path.join(current_root, filename)
            with codecs.open(path, 'rb', encoding) as f:
                content = f.read()
                new_content = content.replace(old, new).replace('\\', '/')
                start = new_content.index(new)
                junk_start = re.search(r'(\.[^\w]){1,2}/',
                                       new_content).start()  # there's definitely no .. or ./ in the absolute path

                source = new_content[start:junk_start - 2].replace('\00', '')
                link_name = filename.replace('\00', '').replace('.lnk', '')
                try:
                    os.symlink(source, os.path.join(current_root, link_name))
                except FileExistsError:
                    pass


if __name__ == '__main__':
    args = parse_args()
    encoding = args.encoding if args.encoding else "ISO-8859-1"

    main(args.root, args.old, args.new, args.encoding)
