const convertInstagramToPhotoSwipe = () => {
  // inner function to return figure html
  // TODO: iranzo figure out the caption
  const getFigureHTML = (image, height, width, thumbnail) => `
     <figure
    itemprop="associatedMedia"
    itemscope
    itemtype="http://schema.org/ImageObject"
  >
    <a
      href="${image}"
      itemprop="contentUrl"
      data-size="${width}x${height}"
    >
      <img
        src="${thumbnail}"
        itemprop="thumbnail"
        alt="Image description"
      />
    </a>
    <figcaption itemprop="caption description">
      Placeholder image from Unsplash
    </figcaption>
  </figure>
    `;

  // Get div.elegant-instagram
  document.querySelectorAll(".elegant-instagram").forEach(ele => {
    // Get instagram-id
    const instagramId = ele.dataset.instagramId;

    fetch(`https://www.instagram.com/p/${instagramId}/?__a=1`)
      .then(response => {
        response.json().then(json => {
          // Get Original image from the json
          const level1 = json.graphql.shortcode_media;

          let divHTML = `<div
                          class="elegant-gallery"
                          itemscope
                          itemtype="http://schema.org/ImageGallery"
                        >`;

          if (
            level1.edge_sidecar_to_children &&
            level1.edge_sidecar_to_children.edges.length > 0
          ) {
            // It is more than one images
            level1.edge_sidecar_to_children.edges.forEach(edge => {
              //  TODO: iranzo add figure
            });
          } else {
            const origImage = level1.display_url;
            const height = level1.dimensions.height;
            const width = level1.dimensions.width;
            const thumbnail = level1.display_resources[0].src;
            divHTML += getFigureHTML(origImage, height, width, thumbnail);
          }

          // Close div
          divHTML += `</div>`;

          // Replace ele with the div
          ele.innerHTML = divHTML;
          ele.replaceWith(ele.children[0]);

          // Trigger PhotoSwipe
          initPhotoSwipeFromDOM(".elegant-gallery");
        });
      })
      .catch(err => console.error("Failed", err));
  });
};

convertInstagramToPhotoSwipe();
