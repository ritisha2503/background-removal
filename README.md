Implemented a real-time background removal system using K-means clustering on webcam frames. Each frame is segmented into color clusters in RGB space, and the largest cluster is identified as the background.

A binary mask is generated to separate foreground and background, followed by morphological operations and smoothing to refine segmentation. The foreground is preserved while the background is replaced with a custom image, simulating a virtual background system.

The pipeline is optimized by resizing frames to enable real-time performance while maintaining segmentation quality.