import os
import cat_service
import platform
import subprocess

def main():
    #Print header
    print_header()
    #Get output folder
    folder = get_or_create_output_folder()
    #Download cats
    download_cats(folder)
    #display the cats
    display_cats(folder)


def print_header():
    print('---------')
    print('CAT FACTORY')
    print('---------')

def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path

def download_cats(folder):
    print('Contacting server...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print("Finished downloading your cats, bro")


def display_cats(folder):
    print('Displaying cats.') 
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg=open', folder])
    else:
        print("We do not support your OS: " + platform.system())

if __name__ == '__main__':
    main()