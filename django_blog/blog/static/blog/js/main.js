document.addEventListener("DOMContentLoaded", function () {
  const postsDiv = document.getElementById("posts");
  postsDiv.innerHTML = "<p>Loading blog posts...</p>";

  // Simulate fetching data from an API
  setTimeout(() => {
    postsDiv.innerHTML = `
            <article>
                <h3>Post Title 1</h3>
                <p>This is the content of the first post.</p>
            </article>
            <article>
                <h3>Post Title 2</h3>
                <p>This is the content of the second post.</p>
            </article>
        `;
  }, 1000);
});
