# File Organizer Script

This Python script organizes files based on their extensions into separate folders. It automatically categorizes files into folders such as Images, Music, Videos, and Documents, making it easier to locate and manage files in a more organized manner.

## Usage

### Prerequisites

Make sure you have Python and Visual Studio Code (VSC) installed on your computer. If you don't have them installed, follow these links to download and install them:

- Python: [Download Python](https://www.python.org/downloads/)
- Visual Studio Code: [Download Visual Studio Code](https://code.visualstudio.com/)

### Installation

1. Clone the repository or download the script file.

2. Open the command line or terminal and navigate to the folder where the script is located.

### Execution

To organize files in a specific folder, follow these steps:

1. Copy the "organize_files.py" file to the folder that you want to organize.

2. Open a terminal or command prompt in that folder.

3. Run the following command:

    ```shell
    python organize_files.py
    ```

   The script will start organizing the files in the folder based on their extensions. Please note that the script excludes itself ("organize_files.py") from the organization process.

4. After the script finishes running, you will find the files sorted into separate folders within the same directory. The files will be categorized into folders such as Images, Music, Videos, and Documents based on their respective extensions.

### Customization

You can customize the file categories and their associated extensions by modifying the "folders" dictionary in the code. Add or remove categories and extensions as per your requirements. Here's an example:

```python
folders = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif'],
    'Music': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Documents': ['.doc', '.docx', '.pdf', '.txt']
}
