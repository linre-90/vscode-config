import subprocess

'''
Created by linre-90.

This script installs most common extension that i use for visual studio code.
Extensions can be added or removed from extensions array as needed.
I take 0 responsibility if this breaks something...
Feel free to use, modify and tailor for personal needs if interested.

Current installed extensions can be obtained with following command.

code --list-extensions | % { "code --install-extension $_" }

'''

# extensions to install
extensions =[
    "akamud.vscode-theme-onedark",
    "alefragnani.Bookmarks",
    "christian-kohler.path-intellisense",
    "CoenraadS.bracket-pair-colorizer",
    "esbenp.prettier-vscode",
    "kamikillerto.vscode-colorize",
    "ms-azuretools.vscode-docker",
    "ms-dotnettools.csharp",
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "ms-toolsai.jupyter-keymap",
    "ms-toolsai.jupyter-renderers",
    "ms-vscode.vscode-typescript-next",
    "PKief.material-icon-theme",
    "VisualStudioExptTeam.vscodeintellicode"
    ]

#visual studio installation commands
command = ["code", "--install-extension"]

print(f"\n\nStarting installation. Will install {len(extensions)} extension. Please wait!\n\n")

#Run installation process
for extension in extensions:

    print("Trying to install -> " + extension)
    output = subprocess.run([command[0], command[1], extension], shell=True, capture_output=True, text=True)
    print(output.stdout)

    # error happened
    if output.returncode != 0:
        print("Installation failed!\n\n")
        raise Exception("Installation not succesfull!", output.stderr)
    


print("\n\nInstallation complete!")
