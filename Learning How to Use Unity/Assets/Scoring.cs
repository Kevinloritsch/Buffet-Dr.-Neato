
using UnityEngine;
using UnityEngine.UI;

public class Scoring : MonoBehaviour
{
    public Transform player;
    public Text scoring;

    // Update is called once per frame
    void Update()
    {
        scoring.text = player.position.z.ToString("0");
    }
}
