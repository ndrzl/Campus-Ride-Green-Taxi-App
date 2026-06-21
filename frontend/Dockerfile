FROM node:20-alpine AS builder
WORKDIR /app

RUN npm install -g pnpm

# Since Docker is already looking inside the frontend folder, remove the "frontend/" prefixes!
COPY package*.json pnpm-lock.yaml* ./ 
RUN pnpm install
COPY . . 

# --- ADDED THIS SECTION SO NEXT.JS CAN SEE THE KEYS AT BUILD TIME ---
ARG NEXT_PUBLIC_SUPABASE_URL
ARG NEXT_PUBLIC_SUPABASE_ANON_KEY

ENV NEXT_PUBLIC_SUPABASE_URL=$NEXT_PUBLIC_SUPABASE_URL
ENV NEXT_PUBLIC_SUPABASE_ANON_KEY=$NEXT_PUBLIC_SUPABASE_ANON_KEY
# ------------------------------------------------------------------

RUN pnpm run build

FROM node:20-alpine AS runner
WORKDIR /app

RUN npm install -g pnpm

COPY --from=builder /app/.next ./.next
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/public ./public
CMD ["pnpm", "start"]