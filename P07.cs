using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Animate : MonoBehaviour
{
    public float speed; // Speed of the object
    private Rigidbody2D rb2d; // Rigidbody component

    // Initialization
    void Start()
    {
        rb2d = GetComponent<Rigidbody2D>(); // Get the Rigidbody2D component
    }

    // Update is called once per physics frame
    void FixedUpdate()
    {
        // Get input for movement
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        // Create movement vector
        var movement = new Vector2(moveHorizontal, moveVertical).normalized * speed * Time.deltaTime;

        // Apply force to the Rigidbody2D
        rb2d.AddForce(movement);
    }
}
