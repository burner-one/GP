using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Microsoft.DirectX;
using Microsoft.DirectX.Direct3D;

namespace Pracamit
{
    public partial class Form1 : Form
    {
        Microsoft.DirectX.Direct3D.Device device; // Direct3D device
        Microsoft.DirectX.Direct3D.Texture texture; // Texture to render
        Microsoft.DirectX.Direct3D.Font font; // Font for text

        public Form1()
        {
            InitializeComponent(); // Initialize form components
            InitDevice(); // Initialize Direct3D device
            InitFont(); // Initialize font
            LoadTexture(); // Load texture from file
        }

        private void InitFont()
        {
            // Create a new font
            System.Drawing.Font f = new System.Drawing.Font("Arial", 16f, FontStyle.Regular);
            font = new Microsoft.DirectX.Direct3D.Font(device, f);
        }

        private void LoadTexture()
        {
            // Load texture from file
            texture = TextureLoader.FromFile(device, @"C:\Users\student\Desktop\sea.jpg", 
                400, 400, 1, 0, Format.A8B8G8R8, Pool.Managed, Filter.Point, Filter.Point, 
                Color.Transparent.ToArgb());
        }

        private void InitDevice()
        {
            // Set up presentation parameters
            PresentParameters pp = new PresentParameters();
            pp.Windowed = true; 
            pp.SwapEffect = SwapEffect.Discard;
            device = new Device(0, DeviceType.Hardware, this, 
                CreateFlags.HardwareVertexProcessing, pp);
        }

        private void Render()
        {
            // Clear the screen and begin scene
            device.Clear(ClearFlags.Target, Color.CornflowerBlue, 0, 1);
            device.BeginScene();
            using (Sprite s = new Sprite(device))
            {
                s.Begin(SpriteFlags.AlphaBlend);
                // Draw the texture and text
                s.Draw2D(texture, new Rectangle(0, 0, 0, 0), 
                          new Rectangle(0, 0, device.Viewport.Width, device.Viewport.Height), 
                          new Point(0, 0), 0f, new Point(0, 0), Color.White);
                font.DrawText(s, ".", new Point(0, 0), Color.White);
                s.End();
            }
            device.EndScene();
            device.Present(); // Present the rendered frame
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Render(); // Render on paint event
        }
    }
}
