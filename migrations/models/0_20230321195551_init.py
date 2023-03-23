from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "pedido" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cliente" VARCHAR(50) NOT NULL,
    "produto" VARCHAR(50) NOT NULL,
    "valor" DOUBLE PRECISION NOT NULL,
    "entregue" BOOL NOT NULL,
    "estado" SMALLINT NOT NULL,
    "timestamp" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "pedido"."estado" IS 'RECEIVED: 1\nCONFIRMED: 2\nDISPATCHED: 3\nDELIVERED: 4\nCANCELED: 5';
COMMENT ON COLUMN "pedido"."timestamp" IS 'o pedido foi criado as';
COMMENT ON TABLE "pedido" IS 'isso referencia um pedido';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
