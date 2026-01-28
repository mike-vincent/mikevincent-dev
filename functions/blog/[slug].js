export async function onRequest(context) {
    const { slug } = context.params;
    const url = new URL(context.request.url);

    if (!slug) {
        return Response.redirect(url.origin + '/', 302);
    }

    // Fetch the static HTML file from /read/slug.html
    const htmlUrl = `${url.origin}/read/${slug}.html`;
    const response = await fetch(htmlUrl, {
        cf: { cacheEverything: true }
    });

    if (!response.ok) {
        return Response.redirect(url.origin + '/', 302);
    }

    return new Response(response.body, {
        headers: {
            'Content-Type': 'text/html;charset=UTF-8',
            'Cache-Control': 'public, max-age=3600'
        }
    });
}
