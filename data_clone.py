import git

# URL of the GitHub repository
repo_url = 'https://github.com/PhonePe/pulse.git'

# Local directory where you want to clone the repository
local_directory = 'phonepe_data'

# Clone the repository
git.Repo.clone_from(repo_url, local_directory)

print("Repository cloned successfully.")