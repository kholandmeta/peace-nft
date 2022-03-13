import json

glb_url = "https://bafybeiegk6rinqnv6xn4idmmnsdgndljry5r7zct23lvgv55os6tznf52m.ipfs.nftstorage.link/glbs/{id}.glb"
image_url = "https://bafybeie4z3xe2q2usvmhhq554zcmyzg2bzeauqvbkrd7gkcimvc6eactji.ipfs.nftstorage.link/images/{id}.jpg"

nft1_name = "Old Town of Kyiv - Peace Maker {id}"
nft1_description = "Ukraine's capital city of Kyiv standing on Dniepr river offers a vivid scenery of a modern cityscape alongside the cobblestone streets of the Old Town."

nft2_name = "Lviv City Hall - Peace Maker {id}"
nft2_description = "The city of Lviv in Ukraine has had a series of town hall buildings dating as far back as 1357. The city hall of Lviv is a UNESCO World Heritage Site and offers a breathtaking view of the surroundings and its history."

external_url = "https://peace.kho.land/"

metadata_path = "./metadatas"

for i in range(0, 100):
    metadata = {}
    if i // 50 < 1:
        metadata["name"] = nft1_name.format(id=i + 1)
        metadata["description"] = nft1_description.format(id=i + 1)
    else:
        metadata["name"] = nft2_name.format(id=i + 1)
        metadata["description"] = nft2_description.format(id=i + 1)
    metadata["animation_url"] = glb_url.format(id=i + 1)
    metadata["image"] = image_url.format(id=i + 1)
    metadata["external_url"] = external_url

    with open("./metadata/{id}".format(id=i + 1), "w") as f:
        json.dump(metadata, f, indent=4)
