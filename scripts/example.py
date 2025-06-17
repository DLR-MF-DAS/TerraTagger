import streamlit as st
import click
import matplotlib.pyplot as plt
import numpy as np

from terratagger.datasource import NPZDirectorySource
from terratagger.sampler import RandomItemSampler

@click.command()
@click.option('-i', '--input-dir', help='NPZ file directory')
def main(input_dir):
    source = NPZDirectorySource(input_dir, '*.npz', ['methane', 'u10', 'v10', 'qa'])
    sampler = RandomItemSampler(source)
    if 'patch' not in st.session_state:
        st.session_state.patch = sampler.get()
    patch = st.session_state.patch
    a = patch['methane'].min()
    b = patch['methane'].max()
    vmin = st.slider("vmin (CH4 ppm)", a, b, a)
    vmax = st.slider("vmax (CH4 ppm)", a, b, b)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7), tight_layout=True)
    x = np.arange(patch['methane'].shape[1])
    y = np.arange(patch['methane'].shape[0])
    xv, yv = np.meshgrid(x, y)
    im1 = ax1.imshow(patch['methane'], vmin=vmin, vmax=vmax)
    ax1.quiver(xv, yv, patch['u10'], patch['v10'])
    im2 = ax2.imshow(patch['qa'])
    fig.colorbar(im1, ax=ax1, shrink=0.8)
    fig.colorbar(im2, ax=ax2, shrink=0.8)
    ax1.set_title("Methane Concentrations & Wind-field")
    ax2.set_title("QA")
    st.pyplot(fig)
    col1, col2 = st.columns([1, 1])
    with col1:
        choice = st.radio("Is there a methane super-emitter in this patch?", ["Yes", "No"])
    with col2:
        go = st.button("Next")
    if go:
        patch = sampler.get()
        st.session_state.patch = patch
        st.rerun()
    
    
    

if __name__ == '__main__':
    main()
