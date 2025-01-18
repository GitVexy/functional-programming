def restore_documents(originals: tuple, backups: tuple):
    return set(
        filter(lambda x : not x.isdigit(),
               map(lambda x : x.upper(),
                   originals + backups)
               )
        )

print(restore_documents(("test1", "test2", "319312"), ("test1", "test2", "test3")))