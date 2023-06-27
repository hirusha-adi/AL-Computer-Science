import os

def generate_index_md():
    with open('index.md', 'w') as f:
        f.write('# Index\n\n')
        
        for root, dirs, files in os.walk('.'):
            # Remove leading "./" from the root path
            root = root[2:]
            
            # Skip the .git folder and _resources folder
            if '.git' in dirs:
                dirs.remove('.git')
                continue
            if '_resources' in dirs:
                dirs.remove('_resources')
                continue
            
            # Skip the current directory if it is the root directory
            if root == '':
                continue
            
            # Write the directory name as a markdown heading
            f.write(f'## {root}\n')
            
            # Write the files in the current directory
            if files:
                f.write('### Files\n\n')
                for file in files:
                    if file.endswith('.md') and file != 'index.md':
                        file_name = os.path.basename(file)
                        file_path = os.path.relpath(os.path.join(root, file)).replace('\\', '/')
                        f.write(f'- [{file_name}]({file_path})\n')
            
            # Write the subdirectories in the current directory
            if dirs:
                f.write('### Subdirectories\n\n')
                for directory in dirs:
                    f.write(f'- {directory}\n')
            
            f.write('\n')

if __name__ == '__main__':
    generate_index_md()
