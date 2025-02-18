
interface GithubEvents {
  type: string,
  repo : {
    name: string
  }
}

export async function getGitUserActivity(username: string) {
  try {
    const response = await fetch(
      `https://api.github.com/users/${username}/events`,
      {
        headers: {
          "User-Agent": "node.js",
        },
      }
    );

    if (!response.ok) {
      throw new Error("Network response was not ok");
    }

    return await response.json();
  } catch (error: unknown) {
    if (error instanceof Error) {
      console.error("There was a problem with the fetch operation:", error);
    } else {
      console.error("An unknown error occurred:", error);
    }
    
    return []; 
  }
}


(async () => {
  const username = process.argv[2]
  if (!username){
    console.log('Github username not provided.')
  }
  else{
    const response: GithubEvents[] = await getGitUserActivity("Yosef-ft");
    response.forEach(gitEvent => {
      console.log(`${gitEvent.type} :: ${gitEvent.repo.name}`)
    });
  }
})();
