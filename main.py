import time
from config import Config
from commands import handle_command, MockClient, MockMessage # Import Mock objects

def run_bot_simulation():
    """
    Simulates the bot receiving messages and processing commands.
    This does NOT connect to actual WhatsApp.
    """
    print(f"\n--- [{Config.BOT_NAME}] Starting bot in SIMULATION mode ---")
    mock_client = MockClient()
    mock_group_chat_id = "1234567890@g.us" # A mock group JID for simulation

    # Initialize user balances in the mock database
    from database import db
    db.get_user("2347010000001@s.whatsapp.net") # User 1
    db.get_user("2347010000002@s.whatsapp.net") # Admin 1
    db.get_user("2347010000003@s.whatsapp.net") # User 2

    while True:
        # --- Simulate a user working ---
        print("\n--- Simulating: User 1 performs '.work' ---")
        user1_jid = "2347010000001@s.whatsapp.net"
        msg1 = MockMessage(
            sender=user1_jid,
            chat_id=mock_group_chat_id,
            text=f"{Config.PREFIX}work",
            is_group=True
        )
        handle_command(mock_client, msg1)
        time.sleep(3)

        # --- Simulate an admin tagging all ---
        print("\n--- Simulating: Admin 1 performs '.tagall' ---")
        admin1_jid = "2347010000002@s.whatsapp.net"
        # Mock members for tagall. In a real bot, these come from the group.
        mock_client.get_group_members = lambda chat_id: [user1_jid, admin1_jid, "2347010000003@s.whatsapp.net"]
        msg2 = MockMessage(
            sender=admin1_jid,
            chat_id=mock_group_chat_id,
            text=f"{Config.PREFIX}tagall",
            is_group=True,
            is_admin=True,
            mentions=[user1_jid, admin1_jid, "2347010000003@s.whatsapp.net"]
        )
        handle_command(mock_client, msg2)
        time.sleep(3)
        
        # --- Simulate a user gambling ---
        print("\n--- Simulating: User 1 performs '.gamble 200' ---")
        msg3 = MockMessage(
            sender=user1_jid,
            chat_id=mock_group_chat_id,
            text=f"{Config.PREFIX}gamble 200",
            is_group=True
        )
        handle_command(mock_client, msg3)
        time.sleep(3)

        # --- Simulate a user asking for owner info ---
        print("\n--- Simulating: User 2 performs '.owner' ---")
        user2_jid = "2347010000003@s.whatsapp.net"
        msg4 = MockMessage(
            sender=user2_jid,
            chat_id=mock_group_chat_id,
            text=f"{Config.PREFIX}owner",
            is_group=True
        )
        handle_command(mock_client, msg4)
        time.sleep(5) # Longer pause before loop repeats

if __name__ == "__main__":
    run_bot_simulation()
