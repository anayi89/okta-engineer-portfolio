const rssFeeds = [
    "https://www.bing.com/news/search?q=Identity%20Management&format=RSS",
    "https://www.bing.com/news/search?q=Access%20Management&format=RSS",
    "https://www.bing.com/news/search?q=Identity%20Access%20Management&format=RSS",
    "https://www.bing.com/news/search?q=Entra%20ID&format=RSS",
    "https://www.bing.com/news/search?q=Okta&format=RSS",
    "https://www.bing.com/news/search?q=CyberArk&format=RSS",
    "https://www.bing.com/news/search?q=SailPoint&format=RSS",
    "https://www.bing.com/news/search?q=ForgeRock&format=RSS",
    "https://www.bing.com/news/search?q=SAML&format=RSS",
    "https://www.bing.com/news/search?q=OIDC&format=RSS",
    "https://www.bing.com/news/search?q=OAuth&format=RSS"
];

async function fetchRSS(url) {
    try {
        const response = await fetch(`https://api.allorigins.win/get?url=${encodeURIComponent(url)}`);
        const data = await response.json();
        const parser = new DOMParser();
        const xml = parser.parseFromString(data.contents, "text/xml");
        return xml;
    } catch (error) {
        console.error("Error fetching RSS feed:", error);
    }
}

async function loadFeeds() {
    const feedContainer = document.getElementById("feed-container");
    for (const url of rssFeeds) {
        const xml = await fetchRSS(url);
        if (xml) {
            const items = xml.querySelectorAll("item");
            items.forEach(item => {
                const title = item.querySelector("title").textContent;
const link = item.querySelector("link").textContent.split("&url=")[1].replaceAll("%3a",":").replaceAll("%2f","/");
                const pubDate = item.querySelector("pubDate")?.textContent;

                const feedItem = document.createElement("div");
                feedItem.classList.add("feed-item");
                feedItem.innerHTML = `
                    <a href="${link}" target="_blank">${title}</a>
                    <p class="date">Published: ${pubDate}</p>
                `;
                feedContainer.appendChild(feedItem);
            });
        }
    }
}

loadFeeds();