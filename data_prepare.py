import os, csv
from shutil import copyfile

def main():
    cwd = os.getcwd()

    count = 5900
    # for dic in os.listdir(cwd):
    for dic in os.listdir(cwd):
        temp = os.path.join(cwd, dic)
        if not os.path.isdir(temp) or dic == 'all':
            continue

        fieldnames = ['name', 'content']

        for subdir, _, files in os.walk(temp):
            data = []
            for file in files:
                name = f'{count}.png'
                content = file.split('_')[0].strip()
                count += 1

                new_data = {
                    'name': name,
                    'content': content
                }

                try:
                    copyfile(os.path.join(cwd, f'{subdir}/{file}'), os.path.join(cwd, f'all/train/{name}'))
                    print('processing: ' + file)
                except:
                    print("Failed to copy file")

                data.append(new_data)

            with open('sentences.csv', 'a') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerows(data)


if __name__ == '__main__':
    main()
                