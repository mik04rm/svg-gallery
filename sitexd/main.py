from fastapi import FastAPI, HTTPException
from typing import List
import sqlite3

app = FastAPI()

# Function to fetch data from SQLite database
def fetch_data(query, params=None):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

@app.get("/tags", response_model=List[dict])
async def get_tags_with_image_count():
    query = """
        SELECT
            appxd_tag.name,
            COUNT(appxd_image.id) AS image_count
        FROM
            appxd_tag
        LEFT JOIN
            appxd_image_tags ON appxd_tag.id = appxd_image_tags.tag_id
        LEFT JOIN
            appxd_image ON appxd_image_tags.image_id = appxd_image.id
        GROUP BY
            appxd_tag.name
    """
    tags_with_count = fetch_data(query)
    tags_data = [{"tag": tag[0], "image_count": tag[1]} for tag in tags_with_count]
    return tags_data



@app.get("/images", response_model=List[dict])
async def get_images_with_tags():
    query = """
        SELECT
            appxd_image.id,
            appxd_image.title,
            appxd_image.description,
            appxd_image.pub_date,
            appxd_image.width,
            appxd_image.height,
            GROUP_CONCAT(appxd_tag.name) AS tags
        FROM
            appxd_image
        LEFT JOIN
            appxd_image_tags ON appxd_image.id = appxd_image_tags.image_id
        LEFT JOIN
            appxd_tag ON appxd_image_tags.tag_id = appxd_tag.id
        GROUP BY
            appxd_image.id
    """
    images_with_tags = fetch_data(query)
    images_data = []
    for image in images_with_tags:
        image_dict = {
            "id": image[0],
            "title": image[1],
            "description": image[2],
            "pub_date": image[3],
            "width": image[4],
            "height": image[5],
            "tags": image[6].split(',') if image[6] else []
        }
        images_data.append(image_dict)
    return images_data


@app.get("/images/{tag}", response_model=List[dict])
async def get_images_by_tag(tag: str):
    query = """
        SELECT
            appxd_image.id,
            appxd_image.title,
            appxd_image.description,
            appxd_image.pub_date,
            appxd_image.width,
            appxd_image.height
        FROM
            appxd_image
        LEFT JOIN
            appxd_image_tags ON appxd_image.id = appxd_image_tags.image_id
        LEFT JOIN
            appxd_tag ON appxd_image_tags.tag_id = appxd_tag.id
        WHERE
            appxd_tag.name = ?
    """
    images_by_tag = fetch_data(query, (tag,))
    images_data = []
    for image in images_by_tag:
        image_dict = {
            "id": image[0],
            "title": image[1],
            "description": image[2],
            "pub_date": image[3],
            "width": image[4],
            "height": image[5]
        }
        images_data.append(image_dict)
    return images_data


def delete_images(image_ids: List[int]):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    for image_id in image_ids:
        cursor.execute("DELETE FROM appxd_image WHERE id=?", (image_id,))
    connection.commit()
    connection.close()

@app.delete("/images/del")
async def delete_images_endpoint(image_ids: List[int]):
    if not image_ids:
        raise HTTPException(status_code=400, detail="No image IDs provided")

    delete_images(image_ids)
    return {"message": "Images deleted successfully"}

# curl -X DELETE "http://127.0.0.1:8000/images/del" -H "Content-Type: application/json" -d "[1, 2, 3]"
# uvicorn main:app --reload
