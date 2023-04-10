<html>
<head>

</head>
<body>
  <h1>CleanUp-Downloads-Folder</h1>
  <p>This repository contains a Python script that moves files from the "Downloads" folder to the "To_delete" folder if they are older than a specified threshold.</p>
  <h2>Requirements</h2>
  <ul>
    <li>Python 3.x</li>
    <li>shutil module</li>
    <li>os module</li>
    <li>time module</li>
  </ul>
  <h2>Usage</h2>
  <ol>
    <li>Set the downloads_folder and to_delete_folder variables to the desired paths.</li>
    <li>Set the age_threshold variable to the desired age threshold for files (in seconds).</li>
    <li>Run the script using a Python interpreter. The script will move files older than the specified age threshold from the downloads_folder to the to_delete_folder.</li>
  </ol>
  <p>Note: If the to_delete_folder does not exist, the script will create it.</p>
  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
</body>
</html>
