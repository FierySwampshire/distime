
if __name__ == '__main__':
    d = ['_CACHED_SLOTS', '_HANDLERS', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '_add_reaction', '_clear_emoji', '_cs_channel_mentions', '_cs_clean_content', '_cs_guild', '_cs_raw_channel_mentions', '_cs_raw_mentions', '_cs_raw_role_mentions', '_cs_system_content', '_edited_timestamp', '_handle_activity', '_handle_application', '_handle_attachments', '_handle_author', '_handle_call', '_handle_content', '_handle_edited_timestamp', '_handle_embeds', '_handle_flags', '_handle_member', '_handle_mention_everyone', '_handle_mention_roles', '_handle_mentions', '_handle_nonce', '_handle_pinned', '_handle_tts', '_handle_type', '_rebind_channel_reference', '_remove_reaction', '_state', '_try_patch', '_update', 'ack', 'activity', 'add_reaction', 'application', 'attachments', 'author', 'call', 'channel', 'channel_mentions', 'clean_content', 'clear_reaction', 'clear_reactions', 'content', 'created_at', 'delete', 'edit', 'edited_at', 'embeds', 'flags', 'guild', 'id', 'is_system', 'jump_url', 'mention_everyone', 'mentions', 'nonce', 'pin', 'pinned', 'publish', 'raw_channel_mentions', 'raw_mentions', 'raw_role_mentions', 'reactions', 'reference', 'remove_reaction', 'reply', 'role_mentions', 'stickers', 'system_content', 'to_message_reference_dict', 'to_reference', 'tts', 'type', 'unpin', 'webhook_id']
    print('{')
    for i in d:
        if i[0] == '_':
            continue
        print(f"\t'{i}':", 'message.', i, ',', sep='')
    print('}')
