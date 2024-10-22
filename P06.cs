using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraShake : MonoBehaviour
{
    public Transform cameraTransform; // Reference to the camera's transform
    private Vector3 _originalPosOfCam; // Original position of the camera
    public float shakeFrequency; // Frequency of the shake

    // Initialization
    void Start()
    {
        _originalPosOfCam = cameraTransform.position; // Store the original position
    }

    // Update is called once per frame
    void Update()
    {
        // Check for shake input
        if (Input.GetKey(KeyCode.S))
        {
            CameraShake(); // Start shaking
        }
        else if (Input.GetKeyUp(KeyCode.S))
        {
            StopShake(); // Stop shaking
        }
    }

    // Apply camera shake
    private void CameraShake()
    {
        cameraTransform.position = _originalPosOfCam + Random.insideUnitSphere * shakeFrequency;
    }

    // Reset camera position
    private void StopShake()
    {
        cameraTransform.position = _originalPosOfCam;
    }
}
