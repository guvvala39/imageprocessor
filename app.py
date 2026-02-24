"""Streamlit web UI for image processing."""

import streamlit as st
import io
import csv
from PIL import Image
import numpy as np
from src.image_processor import process_image


def process_uploaded_file(uploaded_file):
    """Process the uploaded image file."""
    # Save temporary file
    temp_path = "/tmp/temp_image.jpg"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process image
    output_path = "/tmp/output_grayscale.jpg"
    grayscale_img, matrix = process_image(temp_path, output_path)
    
    return grayscale_img, matrix


def matrix_to_csv(matrix):
    """Convert numpy matrix to CSV bytes."""
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write matrix rows
    for row in matrix:
        writer.writerow(row)
    
    return output.getvalue().encode()


def main():
    # Page configuration
    st.set_page_config(
        page_title="Image Processor",
        page_icon="📷",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Title and description
    st.title("📷 Image Processor")
    st.markdown("""
    **Convert images to grayscale & extract data**
    
    Upload a JPEG image to:
    - Crop to 256×256 pixels from the top-center
    - Convert to grayscale
    - Download the processed image and data matrix
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.info("""
        This tool processes images by:
        1. Cropping to **256×256** pixels (top-center)
        2. Converting to **grayscale** (black & white)
        3. Exporting as **image** and **CSV matrix**
        """)
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📤 Upload Image")
        uploaded_file = st.file_uploader(
            "Choose a JPEG image",
            type=["jpg", "jpeg", "png"],
            help="Supported formats: JPEG, PNG"
        )
    
    # Process image if uploaded
    if uploaded_file is not None:
        try:
            with st.spinner("Processing image..."):
                grayscale_img, matrix = process_uploaded_file(uploaded_file)
            
            # Display results
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🖼️ Processed Image")
                st.image(grayscale_img, use_column_width=True, caption="Grayscale 256×256")
            
            with col2:
                st.subheader("📊 Matrix Info")
                col_a, col_b = st.columns(2)
                with col_a:
                    st.metric("Shape", f"{matrix.shape[0]}×{matrix.shape[1]}")
                    st.metric("Data Type", str(matrix.dtype))
                with col_b:
                    st.metric("Min Value", int(matrix.min()))
                    st.metric("Max Value", int(matrix.max()))
                
                st.write("**Sample (first 10×10 values):**")
                st.dataframe(matrix[:10, :10], use_container_width=True)
            
            # Download section
            st.divider()
            st.subheader("⬇️ Download Results")
            
            col_img, col_csv = st.columns(2)
            
            with col_img:
                # Convert PIL image to bytes for download
                img_byte_arr = io.BytesIO()
                grayscale_img.save(img_byte_arr, format='JPEG')
                img_byte_arr.seek(0)
                
                st.download_button(
                    label="📥 Download Image (JPG)",
                    data=img_byte_arr,
                    file_name="output_grayscale.jpg",
                    mime="image/jpeg",
                    use_container_width=True
                )
            
            with col_csv:
                # Convert matrix to CSV
                csv_data = matrix_to_csv(matrix)
                
                st.download_button(
                    label="📥 Download Matrix (CSV)",
                    data=csv_data,
                    file_name="grayscale_matrix.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            
            # Success message
            st.success("✅ Image processed successfully!")
            
        except Exception as e:
            st.error(f"❌ Error processing image: {str(e)}")
            st.info("Make sure the image is a valid JPEG or PNG file.")
    
    else:
        # Empty state
        st.info("👆 Upload an image to get started!")


if __name__ == "__main__":
    main()
