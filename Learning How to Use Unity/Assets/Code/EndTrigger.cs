
using UnityEngine;

public class EndTrigger : MonoBehaviour
{
    public Management gameManager;

    void OnTriggerEnter ()
    {
        gameManager.CompleteLevel();
    }
}
