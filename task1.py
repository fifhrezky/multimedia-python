import moviepy
import moviepy.editor as mp
import pygame
import PIL
import cv2
import pydub
import tkinter as tk
from pkg_resources import get_distribution, DistributionNotFound

def check_installation():
    # Pygame version
    try:
        print("✅ Pygame version:", pygame.__version__)
    except AttributeError:
        print("❌ Pygame version could not be determined")
    
    # Pillow version
    try:
        print("✅ Pillow version:", PIL.__version__)
    except AttributeError:
        print("❌ Pillow version could not be determined")
    
    # OpenCV version
    try:
        print("✅ OpenCV version:", cv2.__version__)
    except AttributeError:
        print("❌ OpenCV version could not be determined")
    
    # MoviePy version
    try:
        moviepy_version = get_distribution("moviepy").version
        print("✅ MoviePy version:", moviepy_version)
    except DistributionNotFound:
        print("❌ MoviePy is not installed")

    # Pydub version
    try:
        pydub_version = get_distribution("pydub").version
        print("✅ Pydub version:", pydub_version)
    except DistributionNotFound:
        print("❌ Pydub is not installed")

    # Tkinter check
    try:
        tk_version = tk.TkVersion
        print(f"✅ Tkinter is installed and working! Version: {tk_version}")
    except Exception as e:
        print(f"❌ Error with Tkinter: {e}")

if __name__ == "__main__":
    check_installation()