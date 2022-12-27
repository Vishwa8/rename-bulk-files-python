import os

# File path
Source_Path = "F:\Docs\other"

# Destination path
Destination = "F:\Docs\Done"


def main():
    for filename in os.listdir(Source_Path):
        # rename all the files
        # remove '<Something>' and rename
        if '<Something>' in filename:
            if not (filename[22] == ' '):
                dst = filename[22:((filename.index(')')) + 1)] + filename[-4:]
                print(dst)
                os.rename(os.path.join(Source_Path, filename),
                          os.path.join(Destination, dst))
            else:
                dst = filename[23:((filename.index(')')) + 1)] + filename[-4:]
                print(dst)
                os.rename(os.path.join(Source_Path, filename),
                          os.path.join(Destination, dst))


# Driver Code
if __name__ == '__main__':
    main()
