#Fetching Github repo information 
import requests

def get_repo_info(owner, repo):
    """Fetch public repository information."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        print("=" * 40)
        print("GITHUB REPOSITORY INFORMATION")
        print("=" * 40)
        print(f"Name        : {data['name']}")
        print(f"Description : {data['description']}")
        print(f"Stars       : {data['stargazers_count']}")
        print(f"Forks       : {data['forks_count']}")
        print(f"Language    : {data['language']}")
        print(f"Default Branch: {data['default_branch']}")
        print(f"Open Issues : {data['open_issues_count']}")
        print("=" * 40)
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot connect to GitHub API")
    except requests.exceptions.Timeout:
        print("Error: Request timed out")

if __name__ == "__main__":
    get_repo_info("python", "cpython")

