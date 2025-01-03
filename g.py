# by chat gpt
import os

header = """# container_aria

My file for learning about container

<p align="center">
  <a href="#introduction">introduction</a> •
  <a href="#table-of-contents">table of contents</a> •
  <a href="#file-list">file_list</a> •
  <a href="#download">Download</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

<p id="introduction"></p>

## 🚀 introduction
this is my container file and learn container

<p align="left"> <a href="#">
    <img alt="Docker" src="https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
    <img alt="Podman" src="https://img.shields.io/badge/-Podman-892CA0?style=flat-square&logo=podman&logoColor=white" />
    <img alt="Kubernetes" src="https://img.shields.io/badge/-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" />
  </a>
</p>

<p id="table-of-contents"></p>

## 📋 Table of Contents

<p id="file-list"></p>

# 📄 File List

"""

footer = """<p id="download"></p>

## 🔨 download

1. Open a terminal or command prompt on your computer.
2. Navigate to the directory where you want to save this project.
3. Use the following command to download the project from the GitHub repository:
   ```sh
   git clone https://github.com/ariafatah0711/container_aria.git
   ```

<p id="related"></p>

## 📈 related

<p id="license"></p>

## ©️ license
<a href="https://github.com/ariafatah0711" alt="CREATED"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=CREATED%20BY&message=ariafatah0711&color=000000"></a>
<a href="https://github.com/ariafatah0711/ariafatah0711/blob/main/LICENSE" alt="LICENSE"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=LICENSE&message=MIT&color=000000"></a>
"""

def collect_data(path, priority_folders, exclude_dirs):
    data = []

    def sort_key(dirpath):
        relative_path = os.path.relpath(dirpath, path).replace("\\", "/")
        if relative_path in priority_folders:
            return (0, priority_folders.index(relative_path))
        elif relative_path.startswith("linux"):
            return (1, relative_path)
        else:
            return (2, relative_path)

    for dirpath, dirnames, filenames in os.walk(path):
        # Ubah dirnames untuk mengecualikan folder di exclude_dirs
        relative_path = os.path.relpath(dirpath, path).replace("\\", "/")
        if any(excluded in relative_path.split("/") for excluded in exclude_dirs):
            continue  # Langsung skip direktori jika ada di exclude_dirs

        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]  # Hapus subdirektori yang dikecualikan
        
        dirnames.sort(key=lambda x: sort_key(os.path.join(dirpath, x)))

        markdown_files = sorted([f for f in filenames if f.endswith('.md')])
        if markdown_files:
            data.append((dirpath, markdown_files))
    
    return data

def generate_file_list(path, type="md"):
    output = ""
    priority_folders = ['docker/docker dasar', 'docker/docker file', 'docker', 'podman']
    exclude_dirs = {".git", "_layouts", "readme", "lab_virtual_with_docker"}
    
    data = collect_data(".", priority_folders, exclude_dirs)

    # for dirpath, dirnames, filenames in os.walk(path):
    for dirpath, markdown_files in data:
        # dirnames[:] = [d for d in dirnames if d not in exclude_dirs] # exclaude

        if dirpath == path:
            continue
        
        # dirnames.sort(key=lambda x: (x not in priority_folders, priority_folders.index(x) if x in priority_folders else x))

        print(dirpath)
        # markdown_files = sorted([f for f in filenames if f.endswith('.md')])
        if markdown_files:
            relative_path = os.path.relpath(dirpath, root_path)
            folder_name = os.path.basename(relative_path)

            # output += f"<details>\n<summary><b>{relative_path}</b></summary>\n\n"
            output += f"<details>\n<summary><b>{relative_path}</b></summary>\n<ul>\n"            

            for file in markdown_files:
                # Ganti spasi dengan %20 untuk URL
                if type == "md":
                  file_path = os.path.join(relative_path, file).replace("\\", "/").replace(" ", "%20")
                if type == "html":
                  file_path = os.path.join(relative_path, file).replace("\\", "/").replace(".md", ".html")

                file = os.path.splitext(file)[0]
                # output += f"- [{file}]({file_path})\n"
                output += f" <li><a href='{file_path}'>{file}</a></li>\n"
              
            output += "</ul>\n"
            output += "\n</details>\n\n"
    return output

root_path = "."
# md
file_list_content_md = generate_file_list(root_path, "md")
markdown_content_md = header + file_list_content_md + footer
# html
file_list_content_html = generate_file_list(root_path, "html")
markdown_content_html = header + file_list_content_html + footer

# write
with open("README.md", "w", encoding='utf-8') as readme:
    readme.write(markdown_content_md)

with open("index.md", "w", encoding='utf-8') as readme:
    readme.write(markdown_content_html)

print("README.md updated successfully!")