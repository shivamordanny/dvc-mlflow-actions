from git import Repo

 repo = Repo(repo_path)
 repo_name = repo.remotes.origin.url.split('.git')[0].split('/')[-1]