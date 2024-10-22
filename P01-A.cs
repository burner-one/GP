using System;
using System.Windows.Forms;
using Microsoft.DirectX;
using Microsoft.DirectX.Direct3D;

namespace Prac1a
{
    public partial class Form1 : Form
    {
        Microsoft.DirectX.Direct3D.Device device; // Direct3D device

        public Form1()
        {
            InitializeComponent();
            InitDevice(); // Initialize the device
        }

        public void InitDevice()
        {
            PresentParameters pp = new PresentParameters
            {
                Windowed = true, // Windowed mode
                SwapEffect = SwapEffect.Discard // Discard swap effect
            };
            device = new Device(0, DeviceType.Hardware, this, CreateFlags.HardwareVertexProcessing, pp);
        }

        public void Render()
        {
            device.Clear(ClearFlags.Target, Color.Orange, 0, 1); // Clear screen
            device.Present(); // Present the back buffer
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Render(); // Render on paint
        }
    }
}
